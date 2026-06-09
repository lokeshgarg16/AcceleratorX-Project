import { useEffect, useState } from 'react'
import { useParams } from 'react-router-dom'
import Badge from '../components/Badge'
import { getLead, updateLeadStatus } from '../api/leads'

const statuses = ['New', 'Contacted', 'Call Booked', 'Enrolled', 'Not Interested']

export default function LeadDetail() {
  const { id } = useParams()
  const [lead, setLead] = useState(null)
  const [error, setError] = useState('')

  useEffect(() => {
    let active = true
    getLead(id)
      .then((data) => active && setLead(data))
      .catch((err) => active && setError(err.message || 'Unable to load lead'))
    return () => {
      active = false
    }
  }, [id])

  const onStatusChange = async (event) => {
    const updated = await updateLeadStatus(id, event.target.value)
    setLead(updated)
  }

  if (error) {
    return <div className="mx-auto max-w-3xl px-4 py-10 text-rose-200">{error}</div>
  }

  if (!lead) {
    return <div className="mx-auto max-w-3xl px-4 py-10 text-sand-100/70">Loading lead...</div>
  }

  return (
    <div className="mx-auto max-w-6xl px-4 py-10 sm:px-6 lg:px-8">
      <div className="grid gap-6 lg:grid-cols-[0.95fr_1.05fr]">
        <section className="glass-card p-6 sm:p-8">
          <span className="section-label">Lead detail</span>
          <h2 className="mt-4 font-display text-3xl font-bold text-sand-50">{lead.contact_name}</h2>
          <p className="mt-2 text-sand-100/75">{lead.contact_email} · {lead.contact_phone}</p>

          <div className="mt-6 flex flex-wrap gap-3">
            <Badge tone={lead.category}>{lead.category}</Badge>
            <Badge tone={lead.follow_up_status}>{lead.follow_up_status}</Badge>
            <Badge>{lead.recommended_program}</Badge>
          </div>

          <div className="mt-6 rounded-3xl border border-white/10 bg-white/5 p-5">
            <label className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Follow-up status</label>
            <select className="mt-3 select-field" value={lead.follow_up_status} onChange={onStatusChange}>
              {statuses.map((status) => (
                <option key={status} value={status}>{status}</option>
              ))}
            </select>
          </div>

          <div className="mt-6 grid gap-4 sm:grid-cols-2">
            <div className="rounded-3xl border border-white/10 bg-white/5 p-5">
              <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Score</p>
              <p className="mt-2 font-display text-3xl font-bold text-accent-500">{lead.lead_score}/100</p>
            </div>
            <div className="rounded-3xl border border-white/10 bg-white/5 p-5">
              <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Readiness</p>
              <p className="mt-2 font-display text-2xl font-bold text-sand-50">{lead.readiness_level}</p>
            </div>
          </div>
        </section>

        <section className="space-y-6">
          <div className="glass-card p-6 sm:p-8">
            <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Full answers</p>
            <div className="mt-4 grid gap-3 text-sm text-sand-100/82">
              {[
                ['User type', lead.user_type],
                ['Current role', lead.current_role],
                ['Education/background', lead.education_background],
                ['AI skill level', lead.ai_skill_level],
                ['Goal', lead.goal],
                ['Timeline', lead.timeline],
                ['Budget readiness', lead.budget_readiness],
                ['Weekly availability', lead.weekly_availability],
                ['Preferred learning mode', lead.preferred_learning_mode],
              ].map(([label, value]) => (
                <div key={label} className="rounded-2xl border border-white/10 bg-ink-900/70 p-4">
                  <p className="text-xs uppercase tracking-[0.22em] text-sand-200/55">{label}</p>
                  <p className="mt-2 leading-7 text-sand-50">{value}</p>
                </div>
              ))}
            </div>
          </div>

          <div className="glass-card p-6 sm:p-8">
            <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Counsellor notes</p>
            <pre className="mt-4 whitespace-pre-wrap rounded-3xl border border-white/10 bg-ink-900/80 p-4 text-sm leading-7 text-sand-100/80">{lead.counsellor_notes}</pre>
          </div>

          <div className="glass-card p-6 sm:p-8">
            <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Next recommended action</p>
            <p className="mt-3 text-sm leading-7 text-sand-100/80">{lead.next_action}</p>
          </div>
        </section>
      </div>
    </div>
  )
}
