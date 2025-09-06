from flask import Flask, request, send_file, render_template, redirect, url_for, flash, after_this_request
import os
import subprocess
import uuid
import threading
import time

app = Flask(__name__)
app.secret_key = 'random_secret_key'  # Needed for flashing messages

SCRAPER_PATH = 'scraper.py'
OUTPUT_FILE = 'upsc_questions.txt'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if not url:
            flash("URL is required!", "error")
            return redirect(url_for('index'))

        output_file = f'output_{uuid.uuid4().hex[:8]}.txt'
        cmd = ['python', SCRAPER_PATH]
        env = os.environ.copy()
        env["URL_TO_SCRAPE"] = url
        env["OUTPUT_FILE"] = output_file

        try:
            subprocess.check_call(cmd, env=env)
        except Exception as e:
            flash(f"Scraping failed: {e}", "error")
            return redirect(url_for('index'))

        @after_this_request
        def remove_file(response):
            def delete_later(path):
                time.sleep(1)  # Wait 1 second to allow file handles to close
                try:
                    if os.path.exists(path):
                        os.remove(path)
                except Exception as e:
                    print(f"Error deleting file: {e}")

            threading.Thread(target=delete_later, args=(output_file,), daemon=True).start()
            return response

        return send_file(output_file, as_attachment=True, conditional=False)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
