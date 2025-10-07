import {useState} from 'react'
import axios from 'axios'
export default function UploadPage(){
  const [file, setFile] = useState(null)
  const [preview, setPreview] = useState(null)
  const [campaignId, setCampaignId] = useState(null)

  async function handleUpload(e){
    e.preventDefault()
    if(!file) return alert('pick a file')
    const fd = new FormData()
    fd.append('file', file)
    const res = await axios.post('/api/upload', fd)
    setPreview(res.data.preview)
    setCampaignId(res.data.campaign_id)
  }

  return (<div style={{padding:20}}>
    <h2>Upload recipients</h2>
    <form onSubmit={handleUpload}>
      <input type='file' accept='.csv,.xlsx' onChange={e=>setFile(e.target.files[0])} />
      <button type='submit'>Upload</button>
    </form>
    {campaignId && <div><strong>Campaign ID:</strong> {campaignId}</div>}
    {preview && <div><h3>Preview</h3><pre>{JSON.stringify(preview, null, 2)}</pre></div>}
  </div>)
}
