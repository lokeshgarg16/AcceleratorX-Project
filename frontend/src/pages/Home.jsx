import { Link } from 'react-router-dom'

const programs = [
  'AI Career Starter',
  'GenAI Builder Program',
  'Agent Engineering Program',
  'RAG and Automation Program',
  'Faculty AI Training',
  'Corporate AI Training',
]

const steps = [
  'Answer 10 smart intake questions',
  'Get a transparent program match and lead score',
  'Pass the lead to counsellors with safe, practical notes',
]

export default function Home() {
  return (
    <div className="mx-auto max-w-7xl px-4 pb-16 sm:px-6 lg:px-8">
      <section className="grid gap-8 py-10 lg:grid-cols-[1.15fr_0.85fr] lg:items-center lg:py-16">
        <div className="space-y-8">
          <span className="section-label">AcceleratorX Program Fit Assessment</span>
          <div className="space-y-5">
            <h1 className="font-display text-5xl font-bold leading-tight text-sand-50 sm:text-6xl">
              Qualify leads and recommend the right AI path with explainable scoring.
            </h1>
            <p className="max-w-2xl text-lg leading-8 text-sand-100/75">
              Use a clean intake flow to identify learner intent, budget readiness, timeline urgency, and program fit - then guide every lead to the most practical AcceleratorX next step.
            </p>
          </div>
          <div className="flex flex-wrap gap-3">
            <Link to="/assessment" className="primary-button">Start Assessment</Link>
            <Link to="/admin" className="secondary-button">Open Admin Dashboard</Link>
          </div>
          <div className="grid gap-4 sm:grid-cols-3">
            {steps.map((step, index) => (
              <div key={step} className="glass-card p-4">
                <div className="mb-3 inline-flex h-8 w-8 items-center justify-center rounded-full bg-accent-500 text-sm font-bold text-ink-950">0{index + 1}</div>
                <p className="text-sm leading-6 text-sand-100/80">{step}</p>
              </div>
            ))}
          </div>
        </div>
        <div className="hero-ring glass-card p-6 sm:p-8">
          <div className="rounded-3xl border border-white/10 bg-white/5 p-6">
            <p className="section-label">Built for</p>
            <div className="mt-5 space-y-4">
              <p className="text-sm uppercase tracking-[0.24em] text-sand-200/70">Programs supported</p>
              <div className="flex flex-wrap gap-2">
                {programs.map((program) => (
                  <span key={program} className="rounded-full border border-white/10 bg-white/5 px-3 py-2 text-sm text-sand-100">{program}</span>
                ))}
              </div>
            </div>
            <div className="mt-8 grid gap-4 sm:grid-cols-2">
              <div className="rounded-2xl bg-ink-900/70 p-4">
                <p className="text-xs uppercase tracking-[0.22em] text-sand-200/60">Lead scoring</p>
                <p className="mt-2 font-display text-2xl font-bold">100-point model</p>
              </div>
              <div className="rounded-2xl bg-ink-900/70 p-4">
                <p className="text-xs uppercase tracking-[0.22em] text-sand-200/60">AI safety</p>
                <p className="mt-2 font-display text-2xl font-bold">No guarantee language</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}
