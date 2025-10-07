import Link from 'next/link'
export default function Home(){
  return (<div style={{padding:20}}>
    <h1>Onboard-Tushar — Demo Frontend</h1>
    <ul>
      <li><Link href='/upload'>Upload CSV/XLSX</Link></li>
      <li><Link href='/dashboard'>Dashboard (scaffold)</Link></li>
    </ul>
  </div>)
}
