import { useState, useEffect } from 'react'
import axios from 'axios'
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts'

const fallbackData = [
  { name: 'Claims', transactions: 142 },
  { name: 'KYC', transactions: 86 },
  { name: 'Payments', transactions: 110 },
]

export function App() {
  const [dashboardData, setDashboardData] = useState<any>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchDashboard = async () => {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/dashboard')
        setDashboardData(response.data)
        setError(null)
      } catch (err) {
        console.error('Failed to fetch dashboard data:', err)
        setError('Failed to load data from backend')
      } finally {
        setLoading(false)
      }
    }
    fetchDashboard()
  }, [])

  const data = dashboardData?.employees
    ? dashboardData.employees.map((emp: any) => ({
        name: emp.process_name,
        transactions: emp.transaction_count,
      }))
    : fallbackData
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6">
      <h1 className="text-3xl font-bold mb-4">Workforce Operations Command Center</h1>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        {['Transactions 338', 'Calls 95', 'Avg Utilization 82.1%', 'Available Capacity 1'].map((k) => (
          <div key={k} className="rounded-2xl bg-slate-900 border border-slate-800 p-4 shadow">{k}</div>
        ))}
      </div>
      <div className="rounded-2xl bg-slate-900 border border-slate-800 p-4 h-80 flex flex-col">
        <h2 className="font-semibold mb-2">Process-wise Transaction Trend</h2>
        <div className="flex-1">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={data}><XAxis dataKey="name"/><YAxis/><Tooltip/><Bar dataKey="transactions" fill="#38bdf8"/></BarChart>
          </ResponsiveContainer>
        </div>
      </div>
      <div className="mt-6 text-slate-300">Workload Radar: 🟢 Available for More Work | 🟠 Optimally Utilized | 🔴 Overutilized</div>
    </div>
  )
}
