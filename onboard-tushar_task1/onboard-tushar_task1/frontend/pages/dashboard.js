import {useState} from 'react'
export default function Dashboard(){
  const [campaignId, setCampaignId] = useState('')
  const [status, setStatus] = useState(null)
  async function getStatus(){
    if(!campaignId) return alert('enter campaign id')
    const res = await fetch(`/api/${campaignId}/status`)
    setStatus(await res.json())
  }
  return (<div style={{padding:20}}>
    <h2>Dashboard (scaffold)</h2>
    <input value={campaignId} onChange={e=>setCampaignId(e.target.value)} placeholder='campaign id'/>
    <button onClick={getStatus}>Get Status</button>
    {status && <pre>{JSON.stringify(status, null, 2)}</pre>}
  </div>)
}
