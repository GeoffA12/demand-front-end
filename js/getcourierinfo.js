let getVehicleInfo = () => {
    let courier = JSON.parse(localStorage.getItem('orderinfo'));
    console.log(courier);
    document.getElementById('licenseplate').innerHTML = courier['licensePlate']
    make = courier['make'];
    make = make.charAt(0).toUpperCase() + make.slice(1);
    model = courier['model'];
    model = model.charAt(0).toUpperCase() + model.slice(1);
    document.getElementById('vehicletype').innerHTML = `${make} ${model}`;
    document.getElementById('eta').innerHTML = `${courier['ETA']} minutes`;
}