var user = localStorage.getItem('username');
let onload = () => {
    document.getElementById('accountName').text = user;
}