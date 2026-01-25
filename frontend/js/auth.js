document.addEventListener("DOMContentLoaded", () => {
  console.log("auth.js loaded");

  const form = document.getElementById("loginForm");
  console.log("FORM:", form);

  if (!form) {
    alert("loginForm not found");
    return;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    console.log("Login clicked");

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch("http://127.0.0.1:8000/api/v1/auth/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password })
    });

    const data = await response.json();
    console.log("LOGIN RESPONSE:", data);

   if (!response.ok) {
  alert("Login failed: " + JSON.stringify(data));
  console.error("STATUS:", response.status, data);
  return;
}


    localStorage.setItem("token", data.access_token);
    localStorage.setItem("role", data.role);

    alert("Login success");

    window.location.href =
      data.role === "AUTHORITY"
        ? "authority.html"
        : "dashboard.html";
  });
});
