fetch(`${BASE}/complaints`, {
  headers: authHeaders()
})
.then(res => res.json())
.then(data => {
  const ul = document.getElementById("all");

  data.forEach(c => {
    const li = document.createElement("li");
    li.innerText = `${c.title} | ${c.status}`;
    ul.appendChild(li);
  });
});
document.getElementById("logoutBtn").addEventListener("click", () => {
  localStorage.clear();
  window.location.href = "index.html";
});
