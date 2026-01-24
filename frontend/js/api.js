const BASE_URL = "http://127.0.0.1:8000/api/v1";

function authHeader() {
  return {
    "Authorization": "Bearer " + localStorage.getItem("token"),
    "Content-Type": "application/json"
  };
}
