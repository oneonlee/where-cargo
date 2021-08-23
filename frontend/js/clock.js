const clockTitle = document.querySelector("time");
const clockTitle1 = document.getElementById("js-clock1");
const clockTitle2 = document.getElementById("js-clock2");

const date = new Date();
const minutes = date.getMinutes();
const hours = date.getHours();

clockTitle1.innerText = `${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}`;
clockTitle2.innerText = `${hours < 10 ? `0${hours}` : hours}:${minutes < 10 ? `0${minutes}` : minutes}`;
