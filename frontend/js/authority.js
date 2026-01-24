async function loadAll() {
  const res = await fetch(`${BASE_URL}/complaints`, {
    headers: authHeader()
  });

  const data = await res.json();
  const box = document.getElementById("allComplaints");

  data.forEach(c => {
    box.innerHTML += `
      <div class="card">
        <h4>${c.title}</h4>
        <p>${c.description}</p>
        <button onclick="resolve('${c.id}')">Resolve</button>
      </div>
    `;
  });
}

async function resolve(id) {
  await fetch(`${BASE_URL}/complaints/${id}/status`, {
    method: "PATCH",
    headers: authHeader(),
    body: JSON.stringify({ status: "RESOLVED" })
  });
  location.reload();
}

loadAll();
