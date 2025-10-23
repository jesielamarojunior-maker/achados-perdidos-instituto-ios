// Exemplo de sincronização manual via JSON compartilhado
// Admin faz upload do JSON atualizado
// Alunos baixam o JSON mais recente

function syncWithServer() {
  // Download do arquivo JSON do servidor
  fetch("/items-updated.json")
    .then((response) => response.json())
    .then((data) => {
      localStorage.setItem("lostItems", JSON.stringify(data));
      displayItems();
      showNotification("Dados sincronizados!", "success");
    });
}

// Chamar a cada 5 minutos ou quando página carrega
setInterval(syncWithServer, 5 * 60 * 1000);
