import { request } from './client'

export function submitAssessment(payload) {
  return request('/api/assessment/submit', {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}

export function listLeads() {
  return request('/api/leads')
}

export function getLead(id) {
  return request(`/api/leads/${id}`)
}

export function updateLeadStatus(id, status) {
  return request(`/api/leads/${id}/status`, {
    method: 'PATCH',
    body: JSON.stringify({ status }),
  })
}
