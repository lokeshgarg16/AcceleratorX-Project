import { Link } from 'react-router-dom'

export default function Layout({ children }) {
  return (
    <div className="page-shell">
      <header className="mx-auto flex w-full max-w-7xl items-center justify-between px-4 py-5 sm:px-6 lg:px-8">
        <Link to="/" className="flex items-center gap-3">
          <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-accent-500 text-ink-950 font-bold shadow-lg shadow-accent-500/30">AX</div>
          <div>
            <p className="font-display text-lg font-bold tracking-wide text-sand-50">AcceleratorX</p>
            <p className="text-xs uppercase tracking-[0.28em] text-sand-200/70">Program Fit Engine</p>
          </div>
        </Link>
        <nav className="hidden items-center gap-3 sm:flex">
          <Link to="/assessment" className="secondary-button">Start Assessment</Link>
          <Link to="/admin" className="secondary-button">Admin</Link>
        </nav>
      </header>
      <main>{children}</main>
    </div>
  )
}
