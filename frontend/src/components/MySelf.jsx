import React, { useContext } from 'react'
import { useNavigate } from 'react-router-dom';
import axios from "axios"
import { MdOutlineLogout } from "react-icons/md";

import { IsLoginContext } from '../contexts/UserContext';

const MySelf = () => {
  const navigate = useNavigate()
  const { IsLogin ,setIsLogin } = useContext(IsLoginContext)
  console.log(IsLogin)
  const LogoutRequest = async () => {
    axios.post("http://127.0.0.1:8080/auth/logout","loguut",{
      withCredentials: true
    }).then((res) => {
      setIsLogin(false)
      navigate("/login")
    }).catch((res) => {
      console.log("res "+res);
    })
  }
  return (
<>
  <div className="text-gray-200 text-2xl">
    Myself
  </div>
  <button onClick={LogoutRequest} className='text-blue-200 text-3xl pt-4'>
    <MdOutlineLogout />
  </button>
</>
  )
}

export default MySelf