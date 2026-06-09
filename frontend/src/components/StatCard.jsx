export default function StatCard({ label, value, hint }) {
  return (
    <div className="glass-card p-5">
      <p className="text-xs uppercase tracking-[0.24em] text-sand-200/70">{label}</p>
      <p className="mt-3 font-display text-3xl font-bold text-sand-50">{value}</p>
      {hint ? <p className="mt-2 text-sm text-sand-100/70">{hint}</p> : null}
    </div>
  )
}
