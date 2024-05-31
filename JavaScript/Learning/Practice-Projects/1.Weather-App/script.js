const apiKey = "5771cb111c33d3a267e57f5a2e90fe55"
const apiUrl = `https://api.openweathermap.org/data/2.5/weather?units=metric&q=mashobra`

async function checkWeather(){
    const response = await fetch(apiUrl + `&appid=${apiKey}`);
    var data = await response.json();

    console.log(data);
}
