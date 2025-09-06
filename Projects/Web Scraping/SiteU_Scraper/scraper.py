import requests
from bs4 import BeautifulSoup
import time
import re
import os

def extract_question_text(element, exclude_nested_lists=True):
    """
    Extract text from an element while optionally excluding nested list content
    """
    if exclude_nested_lists:
        # Clone the element to avoid modifying the original
        temp_element = element.__copy__()
        # Remove nested ol and ul elements
        for nested_list in temp_element.find_all(['ol', 'ul']):
            nested_list.decompose()
        return temp_element.get_text(strip=True)
    else:
        return element.get_text(strip=True)

def scrape_upsc_questions(url):
    """
    Scrape UPSC questions from the provided URL with accordion structure
    """
    
    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }
    
    try:
        # Send GET request
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all accordion containers
        accordion_containers = soup.find_all('div', class_=re.compile(r'wp-block-ub-content-toggle-accordion'))
        
        extracted_data = []
        
        for container in accordion_containers:
            # Extract accordion heading
            heading_element = container.find('p', class_=re.compile(r'wp-block-ub-content-toggle-accordion-title'))
            
            if heading_element:
                # Get the heading text, excluding any nested elements
                heading_text = heading_element.get_text(strip=True)
                
                # Find the content panel associated with this accordion
                content_panel = container.find('div', class_=re.compile(r'wp-block-ub-content-toggle-accordion-content-wrap'))
                
                if content_panel:
                    # Find ALL ordered lists within the content panel
                    ol_elements = content_panel.find_all('ol')
                    
                    if ol_elements:
                        # Collect all li elements from all ol elements
                        all_li_elements = []
                        for ol_idx, ol_element in enumerate(ol_elements):
                            # Only get direct child list items (not nested ones)
                            li_elements = ol_element.find_all('li', recursive=False)
                            all_li_elements.extend(li_elements)
                            print(f"Found OL #{ol_idx + 1} with {len(li_elements)} questions")
                        
                        print(f"Total questions found across all OLs: {len(all_li_elements)}")
                        
                        questions = []
                        processed_nested_lis = set()  # Track processed nested elements
                        
                        for i, li in enumerate(all_li_elements, 1):
                            # Skip if this li is actually a nested element we already processed
                            if li in processed_nested_lis:
                                continue
                                
                            # Extract the main question text from span
                            span_element = li.find('span')
                            if span_element:
                                # Get main question text excluding nested lists
                                question_text = extract_question_text(span_element, exclude_nested_lists=True)
                                
                                # Clean up the question text
                                question_text = re.sub(r'^\d{4}\s*[-:]?\s*', '', question_text)
                                question_text = re.sub(r'\s+', ' ', question_text).strip()
                                
                                if question_text:
                                    questions.append(f"Q{i} - {question_text}")
                                
                                # Check for nested ol (subpoints) within the span
                                nested_ol = span_element.find('ol')
                                if not nested_ol:
                                    # Also check within the li element itself
                                    nested_ol = li.find('ol')
                                
                                if nested_ol:
                                    nested_li_elements = nested_ol.find_all('li', recursive=False)
                                    # Mark these nested elements as processed
                                    for nested_li in nested_li_elements:
                                        processed_nested_lis.add(nested_li)
                                    
                                    for j, nested_li in enumerate(nested_li_elements):
                                        nested_span = nested_li.find('span')
                                        if nested_span:
                                            nested_text = nested_span.get_text(strip=True)
                                        else:
                                            nested_text = nested_li.get_text(strip=True)
                                        
                                        nested_text = re.sub(r'^\d{4}\s*[-:]?\s*', '', nested_text)
                                        nested_text = re.sub(r'\s+', ' ', nested_text).strip()
                                        
                                        if nested_text:
                                            # Use Roman numerals for subpoints
                                            roman_numerals = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
                                            roman_num = roman_numerals[j] if j < len(roman_numerals) else f"({j+1})"
                                            questions.append(f"    {roman_num}. {nested_text}")
                            else:
                                # Fallback: get text from li directly, but check for nested content
                                main_text_parts = []
                                nested_ol = li.find('ol')
                                
                                # Extract text before any nested list
                                for content in li.contents:
                                    if hasattr(content, 'name') and content.name in ['ol', 'ul']:
                                        break
                                    if isinstance(content, str):
                                        main_text_parts.append(content.strip())
                                    else:
                                        main_text_parts.append(content.get_text(strip=True))
                                
                                question_text = ' '.join(main_text_parts).strip()
                                question_text = re.sub(r'^\d{4}\s*[-:]?\s*', '', question_text)
                                question_text = re.sub(r'\s+', ' ', question_text).strip()
                                
                                if question_text:
                                    questions.append(f"Q{i} - {question_text}")
                                
                                # Handle nested content
                                if nested_ol:
                                    nested_li_elements = nested_ol.find_all('li', recursive=False)
                                    # Mark these nested elements as processed
                                    for nested_li in nested_li_elements:
                                        processed_nested_lis.add(nested_li)
                                    
                                    for j, nested_li in enumerate(nested_li_elements):
                                        nested_text = nested_li.get_text(strip=True)
                                        nested_text = re.sub(r'^\d{4}\s*[-:]?\s*', '', nested_text)
                                        nested_text = re.sub(r'\s+', ' ', nested_text).strip()
                                        
                                        if nested_text:
                                            roman_numerals = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x']
                                            roman_num = roman_numerals[j] if j < len(roman_numerals) else f"({j+1})"
                                            questions.append(f"    {roman_num}. {nested_text}")
                        
                        if questions:
                            extracted_data.append({
                                'heading': heading_text,
                                'questions': questions
                            })
                    else:
                        # Fallback: Look for questions in other formats (divs, paragraphs, etc.)
                        print(f"No OL found for heading: {heading_text}")
                        fallback_questions = []
                        
                        # Try to find questions in div elements or other containers
                        question_containers = content_panel.find_all(['div', 'p'], string=re.compile(r'\d+\.\s+'))
                        for i, container in enumerate(question_containers, 1):
                            question_text = container.get_text(strip=True)
                            question_text = re.sub(r'^\d+\.\s*', '', question_text)
                            question_text = re.sub(r'^\d{4}\s*[-:]?\s*', '', question_text)
                            if question_text:
                                fallback_questions.append(f"Q{i} - {question_text}")
                        
                        if fallback_questions:
                            extracted_data.append({
                                'heading': heading_text,
                                'questions': fallback_questions
                            })
                            print(f"Found {len(fallback_questions)} questions using fallback method")
        
        return extracted_data
    
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []
    except Exception as e:
        print(f"Error parsing the webpage: {e}")
        return []

def format_output(data):
    """
    Format the extracted data in the requested format
    """
    formatted_output = []
    
    for section in data:
        formatted_output.append(f"\n{section['heading']}")
        for question in section['questions']:
            formatted_output.append(question)
    
    return '\n'.join(formatted_output)

def save_to_file(data, filename='upsc_questions.txt'):
    """
    Save the extracted data to a text file
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(format_output(data))
        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving to file: {e}")

# Main execution
import os

if __name__ == "__main__":
    url = os.environ.get("URL_TO_SCRAPE", "https://upscpdf.com/history-art-and-culture-upsc-mains-topic-wise-previous-year-questions/#gsc.tab=0")
    output_file = os.environ.get("OUTPUT_FILE", "upsc_questions.txt")
    print("Starting web scraping...")
    time.sleep(1)
    scraped_data = scrape_upsc_questions(url)
    if scraped_data:
        print(f"Successfully extracted {len(scraped_data)} sections")
        formatted_text = format_output(scraped_data)
        print("\n" + "="*50)
        print("EXTRACTED CONTENT:")
        print("="*50)
        print(formatted_text)
        save_to_file(scraped_data, filename=output_file)
        print(f"\nStructured data contains {len(scraped_data)} accordion sections")
    else:
        print("No data could be extracted. Please check the URL and page structure.")

