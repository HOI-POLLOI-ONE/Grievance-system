function toggleRegister() {
  document.getElementById("registerForm").classList.toggle("hidden");
}

document.getElementById("loginForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = email.value;
  const password = password.value;

  const res = await fetch(`${BASE_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();

  if (!res.ok) return alert("Login failed");

  localStorage.setItem("token", data.access_token);
  localStorage.setItem("role", data.role);

  if (data.role === "AUTHORITY") {
    window.location.href = "authority.html";
  } else {
    window.location.href = "dashboard.html";
  }
});

document.getElementById("registerForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = r_email.value;
  const password = r_password.value;

  const res = await fetch(`${BASE_URL}/auth/register`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  if (res.ok) alert("Registered! Please login.");
  else alert("Registration failed");
});
