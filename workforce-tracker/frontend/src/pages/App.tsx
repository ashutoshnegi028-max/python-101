import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts'

const data = [
  { name: 'Claims', transactions: 142 },
  { name: 'KYC', transactions: 86 },
  { name: 'Payments', transactions: 110 },
]

export function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-6">
      <h1 className="text-3xl font-bold mb-4">Workforce Operations Command Center</h1>
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        {['Transactions 338', 'Calls 95', 'Avg Utilization 82.1%', 'Available Capacity 1'].map((k) => (
          <div key={k} className="rounded-2xl bg-slate-900 border border-slate-800 p-4 shadow">{k}</div>
        ))}
      </div>
      <div className="rounded-2xl bg-slate-900 border border-slate-800 p-4 h-80">
        <h2 className="font-semibold mb-2">Process-wise Transaction Trend</h2>
        <ResponsiveContainer width="100%" height="100%">
          <BarChart data={data}><XAxis dataKey="name"/><YAxis/><Tooltip/><Bar dataKey="transactions" fill="#38bdf8"/></BarChart>
        </ResponsiveContainer>
      </div>
      <div className="mt-6 text-slate-300">Workload Radar: 🟢 Available | 🟠 Warm | 🔴 Needs support.</div>
    </div>
  )
}
