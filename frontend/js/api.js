const BASE = "http://127.0.0.1:8000/api/v1";

function authHeaders() {
  const token = localStorage.getItem("token");
  if (!token) location.href = "index.html";

  return {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + token
  };
}
