import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import Badge from '../components/Badge'
import StatCard from '../components/StatCard'
import { listLeads } from '../api/leads'

export default function Admin() {
  const [leads, setLeads] = useState([])
  const [error, setError] = useState('')

  useEffect(() => {
    let active = true
    listLeads()
      .then((data) => active && setLeads(data))
      .catch((err) => active && setError(err.message || 'Unable to load leads'))
    return () => {
      active = false
    }
  }, [])

  const hotCount = leads.filter((lead) => lead.category === 'Hot').length
  const warmCount = leads.filter((lead) => lead.category === 'Warm').length
  const coldCount = leads.filter((lead) => lead.category === 'Cold').length

  return (
    <div className="mx-auto max-w-7xl px-4 py-10 sm:px-6 lg:px-8">
      <div className="flex flex-col gap-4 md:flex-row md:items-end md:justify-between">
        <div>
          <span className="section-label">Admin dashboard</span>
          <h2 className="mt-4 font-display text-4xl font-bold text-sand-50">All qualified leads</h2>
          <p className="mt-3 max-w-2xl text-sand-100/75">Review lead quality, follow-up status, and the recommended AcceleratorX program in one place.</p>
        </div>
        <Link to="/assessment" className="secondary-button w-fit">Add new lead</Link>
      </div>

      <div className="mt-8 grid gap-4 md:grid-cols-3">
        <StatCard label="Hot leads" value={hotCount} hint="80-100 score band" />
        <StatCard label="Warm leads" value={warmCount} hint="60-79 score band" />
        <StatCard label="Cold leads" value={coldCount} hint="40-59 score band" />
      </div>

      {error ? <div className="mt-6 rounded-2xl border border-rose-400/20 bg-rose-500/10 px-4 py-3 text-rose-100">{error}</div> : null}

      <div className="glass-card mt-8 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="min-w-full divide-y divide-white/10 text-left">
            <thead className="bg-white/5 text-xs uppercase tracking-[0.2em] text-sand-200/60">
              <tr>
                <th className="px-5 py-4">Name</th>
                <th className="px-5 py-4">Email / Phone</th>
                <th className="px-5 py-4">User type</th>
                <th className="px-5 py-4">Goal</th>
                <th className="px-5 py-4">Program</th>
                <th className="px-5 py-4">Score</th>
                <th className="px-5 py-4">Category</th>
                <th className="px-5 py-4">Timeline</th>
                <th className="px-5 py-4">Budget</th>
                <th className="px-5 py-4">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-white/8 text-sm text-sand-100/80">
              {leads.map((lead) => (
                <tr key={lead.id} className="hover:bg-white/5">
                  <td className="px-5 py-4 font-medium text-sand-50">
                    <Link to={`/admin/leads/${lead.id}`} className="hover:text-accent-500">{lead.contact_name}</Link>
                  </td>
                  <td className="px-5 py-4">
                    <div>{lead.contact_email}</div>
                    <div className="text-sand-200/60">{lead.contact_phone}</div>
                  </td>
                  <td className="px-5 py-4">{lead.user_type}</td>
                  <td className="px-5 py-4 max-w-xs truncate">{lead.goal}</td>
                  <td className="px-5 py-4">{lead.recommended_program}</td>
                  <td className="px-5 py-4 font-semibold text-accent-500">{lead.lead_score}</td>
                  <td className="px-5 py-4"><Badge tone={lead.category}>{lead.category}</Badge></td>
                  <td className="px-5 py-4">{lead.timeline}</td>
                  <td className="px-5 py-4">{lead.budget_readiness}</td>
                  <td className="px-5 py-4"><Badge tone={lead.follow_up_status}>{lead.follow_up_status}</Badge></td>
                </tr>
              ))}
              {!leads.length ? (
                <tr>
                  <td className="px-5 py-10 text-center text-sand-100/70" colSpan="10">No leads yet. Submit the assessment to populate the dashboard.</td>
                </tr>
              ) : null}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
