// Configuração da API
class AchadosAPI {
  constructor() {
    // URL da API - Vercel detecta automaticamente
    this.baseURL =
      window.location.hostname === "localhost"
        ? "http://localhost:8001" // Desenvolvimento local
        : window.location.origin; // Produção (mesmo domínio)

    this.headers = {
      "Content-Type": "application/json",
    };
  }

  // ========== ITEMS ==========
  async getItems() {
    try {
      const response = await fetch(`${this.baseURL}/api/items`);
      if (!response.ok) throw new Error("Erro ao buscar items");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  async createItem(itemData) {
    try {
      const response = await fetch(`${this.baseURL}/api/items`, {
        method: "POST",
        headers: this.headers,
        body: JSON.stringify(itemData),
      });
      if (!response.ok) throw new Error("Erro ao criar item");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  async deleteItem(itemId) {
    try {
      const response = await fetch(`${this.baseURL}/api/items/${itemId}`, {
        method: "DELETE",
      });
      if (!response.ok) throw new Error("Erro ao deletar item");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  // ========== COMENTÁRIOS ==========
  async getComments(itemId) {
    try {
      const response = await fetch(
        `${this.baseURL}/api/items/${itemId}/comments`
      );
      if (!response.ok) throw new Error("Erro ao buscar comentários");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      return [];
    }
  }

  async addComment(itemId, author, text) {
    try {
      const response = await fetch(
        `${this.baseURL}/api/items/${itemId}/comments`,
        {
          method: "POST",
          headers: this.headers,
          body: JSON.stringify({
            author: author,
            text: text,
          }),
        }
      );
      if (!response.ok) throw new Error("Erro ao adicionar comentário");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  // ========== CLAIMS ==========
  async claimItem(itemId, claimerName) {
    try {
      const response = await fetch(
        `${this.baseURL}/api/items/${itemId}/claim`,
        {
          method: "POST",
          headers: this.headers,
          body: JSON.stringify({
            claimer_name: claimerName,
          }),
        }
      );
      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Erro ao reclamar item");
      }
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  async getClaimedItems() {
    try {
      const response = await fetch(`${this.baseURL}/api/claimed-items`);
      if (!response.ok) throw new Error("Erro ao buscar items reclamados");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  async restoreItem(itemId) {
    try {
      const response = await fetch(
        `${this.baseURL}/api/items/${itemId}/restore`,
        {
          method: "POST",
        }
      );
      if (!response.ok) throw new Error("Erro ao restaurar item");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  async confirmDelivery(itemId) {
    try {
      const response = await fetch(
        `${this.baseURL}/api/items/${itemId}/deliver`,
        {
          method: "POST",
        }
      );
      if (!response.ok) throw new Error("Erro ao confirmar entrega");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  // ========== AUTENTICAÇÃO ==========
  async login(password) {
    try {
      const response = await fetch(`${this.baseURL}/api/auth/login`, {
        method: "POST",
        headers: this.headers,
        body: JSON.stringify({
          password: password,
        }),
      });

      if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || "Senha incorreta");
      }

      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  // ========== RESET ==========
  async resetData() {
    try {
      const response = await fetch(`${this.baseURL}/api/reset`, {
        method: "POST",
      });
      if (!response.ok) throw new Error("Erro ao resetar dados");
      return await response.json();
    } catch (error) {
      console.error("Erro:", error);
      throw error;
    }
  }

  // ========== HEALTH CHECK ==========
  async checkHealth() {
    try {
      const response = await fetch(`${this.baseURL}/`);
      return response.ok;
    } catch (error) {
      return false;
    }
  }
}

// Instância global da API
const achadosAPI = new AchadosAPI();
