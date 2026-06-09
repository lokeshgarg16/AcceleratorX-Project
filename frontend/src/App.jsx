import { Navigate, Route, Routes } from 'react-router-dom'
import Layout from './components/Layout'
import Home from './pages/Home'
import Assessment from './pages/Assessment'
import Result from './pages/Result'
import Admin from './pages/Admin'
import LeadDetail from './pages/LeadDetail'

export default function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/assessment" element={<Assessment />} />
        <Route path="/result/:id" element={<Result />} />
        <Route path="/admin" element={<Admin />} />
        <Route path="/admin/leads/:id" element={<LeadDetail />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Layout>
  )
}
