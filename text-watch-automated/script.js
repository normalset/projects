setInterval(updateTime, 1000);

function on(className) {
  console.log("onning ", className)
  const elements = document.getElementsByClassName(className);
  const elementsArray = Array.from(elements); // Convert HTMLCollection to an array

  // Add the class "on" to each element in the array
  elementsArray.forEach((element) => {
    element.classList.add('on');
    element.classList.remove('off')
  });
}

function off(className) {
  console.log('offing ', className)
  const elements = document.getElementsByClassName(className);
  const elementsArray = Array.from(elements); // Convert HTMLCollection to an array

  // Add the class "on" to each element in the array
  elementsArray.forEach((element) => {
    element.classList.add('off');
    element.classList.remove('on')
  });
}

function colorAM(color){
  let am = document.getElementsByClassName('am');
  let pm = document.getElementsByClassName('pm')
  let amArray = Array.from(am);
  let pmArray = Array.from(pm)


  amArray.forEach((element) => {
    element.classList.add(color);
  });
  pmArray.forEach((element) => {
    element.classList.remove(color)
  })
}

function colorPM(color){
  let am = document.getElementsByClassName('am');
  let pm = document.getElementsByClassName('pm')
  let amArray = Array.from(am);
  let pmArray = Array.from(pm)


  amArray.forEach((element) => {
    element.classList.remove(color)
  });
  pmArray.forEach((element) => {
    element.classList.add(color)
  })
}

function colorBorder(color){
  let target = document.getElementsByClassName('clock')[0]
   color=='dayColor'?target.classList.add('dayColor'):target.classList.remove('nightColor')
}

function updateTime() {
  // Get the current time
  const now = new Date();
  let hours = now.getHours();
  let minutes = now.getMinutes();
  let isDay = true
  console.log(hours , minutes)
  // Adjust hours for 12-hour clock
  if (hours > 12) {
    hours = hours - 12;
    on('pm')
    off('am')
    isDay = false
  } else {
    on('am')
    off('pm')
    isDay = true
  }
  if(minutes >=0 && minutes <5){
    off('five-up')
    off('to')
    on('oclock')
  }
  if(minutes >=5 && minutes <10){
    off('oclock')
    on('five-up')
    on('past')
  }
  if(minutes >=10 && minutes <15){
    off('five-up')
    on('ten-up')
    on('past')
  }
  if(minutes >= 15 && minutes <20){
    off('ten-up')
    on('a')
    on('quarter')
    on('past')
  }
  if(minutes >= 20 && minutes < 25){
    off('a')
    off('quarter')
  
    on('twenty')
    on('past')
  }
  if(minutes >=25 && minutes < 30){
    on('twenty')
    on('five-up')
    on('past')
  }
  if(minutes >=30 && minutes < 35){
    off('twenty')
    off('five-up')
    on('half')
    on('past')
  }
  if(minutes > 35) hours++ 
  
  if(minutes >= 35 && minutes < 40){
    off('past')
    on('twenty')
    on('five-up')
    on('to')
  }
  if(minutes >= 40 && minutes < 45){
    off('five-up')
    on('twenty')
    on('to')
  }
  if(minutes >=45 && minutes < 50){
    off('twenty')
    on('a')
    on('quarter')
    on('to')
  }
  if(minutes >= 50 && minutes <55){
    off('a')
    off('quarter')
    on('ten-up')
    on('to')
  }
  if(minutes >= 55 && minutes <60){
    off('ten')
    off('to')
    on('five-up')
    on('to')
  }
  switch(hours){
    case 1:
      off('twelve')
      on('one')
      isDay?colorAM('nightColor'):colorPM('dayColor')
      isDay?colorBorder('nightColor'):colorBorder('dayColor')
      break;
    case 2:
      off('one')
      on('two')
      isDay?colorAM('nightColor'):colorPM('dayColor')
      isDay?colorBorder('nightColor'):colorBorder('dayColor')
      break;
    case 3:
      off('two')
      on('three')
      isDay?colorAM('nightColor'):colorPM('dayColor')
      isDay?colorBorder('nightColor'):colorBorder('dayColor')
      break;
    case 4:
      off('three')
      on('four')
      isDay?colorAM('nightColor'):colorPM('dayColor')
      isDay?colorBorder('nightColor'):colorBorder('dayColor')
      break;
    case 5:
      off('four')
      on('five-down')
      isDay?colorAM('nightColor'):colorPM('dayColor')
      isDay?colorBorder('nightColor'):colorBorder('dayColor')
      break;
    case 6:
      off('five-down')
      on('six')
      isDay?colorAM('dayColor'):colorPM('nightColor')
      isDay?colorBorder('dayColor'):colorBorder('nightColor')
      break;
    case 7:
      off('six')
      on('seven')
      isDay?colorAM('dayColor'):colorPM('nightColor')
      isDay?colorBorder('dayColor'):colorBorder('nightColor')
      break;
    case 8:
      off('seven')
      on('eight')
      isDay?colorAM('dayColor'):colorPM('nightColor')
      isDay?colorBorder('dayColor'):colorBorder('nightColor')
      break;
    case 9:
      off('eight')
      on('nine')
      isDay?colorAM('dayColor'):colorPM('nightColor')
      isDay?colorBorder('dayColor'):colorBorder('nightColor')
      break;
    case 10:
      off('nine')
      on('ten-down')
      isDay?colorAM('dayColor'):colorPM('nightColor')
      isDay?colorBorder('dayColor'):colorBorder('nightColor')
      break;
    case 11:
      off('ten-down')
      on('eleven')
      isDay?colorAM('dayColor'):colorPM('nightColor')
      isDay?colorBorder('dayColor'):colorBorder('nightColor')
      break;
    case 12:
      off('eleven')
      on('twelve')
      isDay?colorAM('dayColor'):colorPM('nightColor')
      isDay?colorBorder('dayColor'):colorBorder('nightColor')
      break;
    case 0:
      off('eleven')
      on('twelve')
      isDay?colorAM('nightColor'):colorPM('dayColor')
      isDay?colorBorder('nightColor'):colorBorder('dayColor')
      break;
  }
}



