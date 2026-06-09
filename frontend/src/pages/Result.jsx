import { useEffect, useState } from 'react'
import { Link, useParams } from 'react-router-dom'
import Badge from '../components/Badge'
import { getLead } from '../api/leads'

export default function Result() {
  const { id } = useParams()
  const [lead, setLead] = useState(null)
  const [error, setError] = useState('')

  useEffect(() => {
    let active = true
    getLead(id)
      .then((data) => active && setLead(data))
      .catch((err) => active && setError(err.message || 'Unable to load result'))
    return () => {
      active = false
    }
  }, [id])

  if (error) {
    return <div className="mx-auto max-w-3xl px-4 py-10 text-rose-200">{error}</div>
  }

  if (!lead) {
    return <div className="mx-auto max-w-3xl px-4 py-10 text-sand-100/70">Loading result...</div>
  }

  return (
    <div className="mx-auto max-w-6xl px-4 py-10 sm:px-6 lg:px-8">
      <div className="grid gap-6 lg:grid-cols-[1.1fr_0.9fr]">
        <section className="glass-card p-6 sm:p-8">
          <span className="section-label">Assessment result</span>
          <h2 className="mt-4 font-display text-4xl font-bold text-sand-50">{lead.recommended_program}</h2>
          <p className="mt-4 text-lg leading-8 text-sand-100/78">{lead.recommendation_reason}</p>

          <div className="mt-6 flex flex-wrap gap-3">
            <Badge tone={lead.category}>{lead.category}</Badge>
            <Badge tone={lead.follow_up_status}>{lead.follow_up_status}</Badge>
            <Badge>{lead.readiness_level}</Badge>
          </div>

          <div className="mt-8 grid gap-4 sm:grid-cols-2">
            <div className="rounded-3xl border border-white/10 bg-white/5 p-5">
              <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Lead score</p>
              <p className="mt-2 font-display text-4xl font-bold text-accent-500">{lead.lead_score}/100</p>
            </div>
            <div className="rounded-3xl border border-white/10 bg-white/5 p-5">
              <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Skill gap summary</p>
              <p className="mt-2 text-sm leading-7 text-sand-100/80">{lead.skill_gap_summary}</p>
            </div>
          </div>

          <div className="mt-6 rounded-3xl border border-white/10 bg-ink-900/70 p-5">
            <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Next step</p>
            <p className="mt-2 text-base leading-7 text-sand-100/85">{lead.next_step}</p>
          </div>
        </section>

        <aside className="space-y-6">
          <div className="glass-card p-6">
            <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">What happens next</p>
            <p className="mt-3 text-sm leading-7 text-sand-100/80">A counsellor can review the lead in the admin dashboard, read the AI-generated notes, and choose the right follow-up status.</p>
            <div className="mt-5 flex flex-wrap gap-3">
              <Link to="/admin" className="primary-button">Open Admin</Link>
              <Link to="/assessment" className="secondary-button">Submit another lead</Link>
            </div>
          </div>

          <div className="glass-card p-6">
            <p className="text-xs uppercase tracking-[0.24em] text-sand-200/60">Counsellor notes</p>
            <pre className="mt-4 whitespace-pre-wrap rounded-3xl border border-white/10 bg-ink-900/80 p-4 text-sm leading-7 text-sand-100/80">{lead.counsellor_notes}</pre>
          </div>
        </aside>
      </div>
    </div>
  )
}
