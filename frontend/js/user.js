loadComplaints();

async function loadComplaints() {
  const res = await fetch(`${BASE}/complaints/my-complaints`, {
    headers: authHeaders()
  });

  const data = await res.json();
  const list = document.getElementById("list");
  list.innerHTML = "";

  data.forEach(c => {
    const li = document.createElement("li");
    li.innerText = `${c.title} — ${c.status}`;
    list.appendChild(li);
  });
}

async function createComplaint() {
  const title = document.getElementById("title").value;
  const description = document.getElementById("desc").value;

  await fetch(`${BASE}/complaints`, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify({ title, description })
  });

  loadComplaints();
}
document.getElementById("logoutBtn").addEventListener("click", () => {
  localStorage.clear();
  window.location.href = "index.html";
});
