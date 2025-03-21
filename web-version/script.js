function convertTemperature() {
    const temp = parseFloat(document.getElementById('temperature').value);
    const conversionType = document.getElementById('conversion').value;
    let result;

    if (isNaN(temp)) {
      document.getElementById('result').textContent = "Please enter a valid number!";
      return;
    }

    if (conversionType === "CtoF") {
      result = (temp * 9 / 5) + 32;
      document.getElementById('result').textContent = `${result.toFixed(2)} °F`;
    } else if (conversionType === "FtoC") {
      result = (temp - 32) * 5 / 9;
      document.getElementById('result').textContent = `${result.toFixed(2)} °C`;
    }
  }