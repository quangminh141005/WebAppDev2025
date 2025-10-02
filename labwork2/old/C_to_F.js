function celsiusToFahrenheit(celcius) {
    return (celcius * 9/5) + 32;
}

function fahrenheitToCelcius(fahrenheit) {
    return (fahrenheit - 32) * 5/9;
}

let celsius = 25;
let fahrenheit = 77;

console.log(celsius + "*C =" + celsiusToFahrenheit(celsius) + "*F")