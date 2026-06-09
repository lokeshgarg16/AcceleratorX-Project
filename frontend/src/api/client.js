const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  })

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Request failed' }))
    const detail = error.detail
    const message = Array.isArray(detail)
      ? detail.map((entry) => entry?.msg || entry?.message || 'Request failed').join(', ')
      : detail

    throw new Error(message || 'Request failed')
  }

  return response.json()
}

export { API_BASE_URL, request }
