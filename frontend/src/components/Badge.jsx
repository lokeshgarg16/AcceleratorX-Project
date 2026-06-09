const statusColors = {
  Hot: 'bg-rose-500/15 text-rose-200 border-rose-400/30',
  Warm: 'bg-amber-500/15 text-amber-200 border-amber-400/30',
  Cold: 'bg-sky-500/15 text-sky-200 border-sky-400/30',
  'Not Suitable': 'bg-slate-500/20 text-slate-200 border-slate-400/30',
  New: 'bg-slate-500/20 text-slate-200 border-slate-400/30',
  Contacted: 'bg-cyan-500/15 text-cyan-200 border-cyan-400/30',
  'Call Booked': 'bg-violet-500/15 text-violet-200 border-violet-400/30',
  Enrolled: 'bg-emerald-500/15 text-emerald-200 border-emerald-400/30',
  'Not Interested': 'bg-rose-500/15 text-rose-200 border-rose-400/30',
}

export default function Badge({ children, tone = children }) {
  return (
    <span className={`inline-flex items-center rounded-full border px-3 py-1 text-xs font-semibold ${statusColors[tone] || 'bg-white/10 text-sand-100 border-white/10'}`}>
      {children}
    </span>
  )
}
