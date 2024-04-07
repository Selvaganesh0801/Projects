//let getWeather=async (city)=>{
    // let weatherApi='https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=1435318a93eafa883b901165632116e5&units=metric';
    // let weatherObj=await fetch(weatherApi);
    // let response=weatherObj.json();
    // return response;
    // }
    
    // async function calWeather(){
    // getWeather('salem')
    // .then((response)=>{
    // console.log(response)
    // console.log('Country:',response['sys']['country'])
    // })
    // }
    // calWeather();

    const searchBox = document.querySelector('.search input');
    const searchBtn = document.querySelector('.search button');
    const icon = document.querySelector('.dyanmic-icon');
    
    searchBtn.addEventListener('click', () => {
      // not empty if
      if (searchBox.value.trim()) {
        checkWeather(searchBox.value.trim());
      } else {
        // empty error
        alert('Plz Enter City');
      }
    });
    
    async function checkWeather(city) {
      const dynamicApi = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=1435318a93eafa883b901165632116e5&units=metric`;
      const response = await fetch(dynamicApi);
      let data = await response.json();
      console.log(data);
      if (data.cod === 200) {
        document.querySelector('.city').innerHTML = data.name;
        document.querySelector('.temp').innerHTML =
          Math.round(data.main.temp) + '°C';
        document.querySelector('.humidity').innerHTML = data.main.humidity + '%';
        document.querySelector('.wind-spead').innerHTML = data.wind.speed + 'Km/h';
        const dymaicIcon = `https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png`;
        icon.src = dymaicIcon;
      } else {
        alert(data.message);
      }
    }
