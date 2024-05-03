import axios from "axios"
import { useEffect, useState } from "react"


const MainContent = () => {
  const [ res, SetData ] = useState()
  useEffect(() => {
    axios.get("http://127.0.0.1:8080/", {}, {}).then((res) => {
      console.log(res.data)
      SetData(res.data)
    }
    )
  }, [])
  return (
<>
  <div className="text-gray-200 text-3xl">
    Main Content
    {res && <div className="text-blue-200">{res.msg}</div>}
  </div>
</>
  )
}

export default MainContent