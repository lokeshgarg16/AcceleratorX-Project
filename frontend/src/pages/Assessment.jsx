import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { submitAssessment } from '../api/leads'

const initialState = {
  user_type: '',
  current_role: '',
  education_background: '',
  ai_skill_level: '',
  goal: '',
  timeline: '',
  budget_readiness: '',
  weekly_availability: '',
  preferred_learning_mode: '',
  contact_name: '',
  contact_email: '',
  contact_phone: '',
}

const selectOptions = {
  user_type: ['Student', 'Working professional', 'Job seeker', 'Independent learner', 'Faculty', 'Corporate team'],
  ai_skill_level: ['Beginner', 'Basic', 'Intermediate', 'Advanced'],
  timeline: ['Immediately', 'Within 1 month', '1-3 months', 'This quarter', '6 months', 'Flexible'],
  budget_readiness: ['Budget ready', 'Can pay with planning', 'Need a flexible option', 'Need more time', 'Not ready yet'],
  weekly_availability: ['2-4 hours', '5-6 hours', '7-10 hours', '10+ hours'],
  preferred_learning_mode: ['Live cohort', 'Mentor-led projects', 'Self-paced', 'Blended workshop'],
}

export default function Assessment() {
  const navigate = useNavigate()
  const [form, setForm] = useState(initialState)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  const updateField = (field) => (event) => {
    setForm((current) => ({ ...current, [field]: event.target.value }))
  }

  const handleSubmit = async (event) => {
    event.preventDefault()
    setLoading(true)
    setError('')
    try {
      const lead = await submitAssessment(form)
      navigate(`/result/${lead.id}`)
    } catch (submissionError) {
      setError(submissionError.message || 'Failed to submit assessment')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mx-auto max-w-5xl px-4 py-10 sm:px-6 lg:px-8">
      <div className="glass-card p-6 sm:p-8">
        <span className="section-label">10-question intake</span>
        <h2 className="mt-4 font-display text-3xl font-bold text-sand-50">Program fit assessment</h2>
        <p className="mt-3 max-w-2xl text-sand-100/75">
          Capture the essentials once, then let the engine recommend the most relevant AcceleratorX program with a practical lead score and follow-up path.
        </p>

        <form className="mt-8 grid gap-5 md:grid-cols-2" onSubmit={handleSubmit}>
          {Object.entries(selectOptions).map(([field, options]) => (
            <label key={field} className="space-y-2">
              <span className="text-sm font-medium text-sand-100/80">{field.replaceAll('_', ' ')}</span>
              <select className="select-field" value={form[field]} onChange={updateField(field)} required>
                <option value="">Select an option</option>
                {options.map((option) => (
                  <option key={option} value={option}>{option}</option>
                ))}
              </select>
            </label>
          ))}

          <label className="space-y-2 md:col-span-2">
            <span className="text-sm font-medium text-sand-100/80">Current role</span>
            <input className="input-field" value={form.current_role} onChange={updateField('current_role')} placeholder="Example: Product manager, student, founder, teacher" required />
          </label>

          <label className="space-y-2 md:col-span-2">
            <span className="text-sm font-medium text-sand-100/80">Education / background</span>
            <textarea className="input-field min-h-28" value={form.education_background} onChange={updateField('education_background')} placeholder="Tell us about your education, skills, or relevant experience" required />
          </label>

          <label className="space-y-2 md:col-span-2">
            <span className="text-sm font-medium text-sand-100/80">Goal</span>
            <textarea className="input-field min-h-28" value={form.goal} onChange={updateField('goal')} placeholder="What do you want to achieve with AI?" required />
          </label>

          <label className="space-y-2 md:col-span-2">
            <span className="text-sm font-medium text-sand-100/80">Contact name</span>
            <input className="input-field" value={form.contact_name} onChange={updateField('contact_name')} required />
          </label>

          <label className="space-y-2">
            <span className="text-sm font-medium text-sand-100/80">Email</span>
            <input type="email" className="input-field" value={form.contact_email} onChange={updateField('contact_email')} required />
          </label>

          <label className="space-y-2">
            <span className="text-sm font-medium text-sand-100/80">Phone</span>
            <input className="input-field" value={form.contact_phone} onChange={updateField('contact_phone')} required />
          </label>

          {error ? <p className="md:col-span-2 rounded-2xl border border-rose-400/20 bg-rose-500/10 px-4 py-3 text-sm text-rose-100">{error}</p> : null}

          <div className="md:col-span-2 flex flex-wrap gap-3 pt-2">
            <button className="primary-button disabled:cursor-not-allowed disabled:opacity-60" type="submit" disabled={loading}>
              {loading ? 'Submitting...' : 'Get Recommendation'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
