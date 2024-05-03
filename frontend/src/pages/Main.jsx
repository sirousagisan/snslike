import React from 'react'
import MainContent from "../components/MainContent"
import MySelf from "../components/MySelf"
import Sidebar from "../components/SideBar"

const Main = () => {
  return (
<>
  <div className="grid grid-cols-9 grid-flow-col text-center h-screen border">
    <div className="col-start-2 col-span-2 row-span-1 border">
      <div className="text-blue-200 text-3xl mt-8">
        SNS-like
      </div>
    </div>
    <div className="col-start-2 col-span-2 row-start-3 border">
      <MySelf/>
    </div>
    <div className="col-start-4 col-span-3 border">
      <MainContent />
    </div>
    <div className="col-start-7 col-span-2 row-span-2 border mt-16">
      <Sidebar />
    </div>
  </div>
</>
  )
}

export default Main