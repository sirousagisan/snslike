import React, {useState, useEffect} from 'react'
import { useNavigate } from 'react-router-dom'
import axios from "axios"

import { Link } from 'react-router-dom'

const Register = () => {
  const [ User, setUser ] = useState({"username": "", "password": "", "email": ""})
  const navigate = useNavigate()
  const RegiserRequest = async () => {
    axios.post("http://127.0.0.1:8080/auth/register", User,{
      withCredentials: true
    }).then((res) => {
      setUser({"username": "", "password": "", "email": ""})
      navigate("/login", {state: {"msg":"アカウントを作成しました。"}})
    }).catch((res) => {
      setUser({"username": "", "password": "", "email": ""})

    })
  }
  return (
<>
<div className="flex justify-center items-center h-screen">
    <div className="border-2 rounded-xl py-8 px-12">
      <div className="text-gray-300 text-3xl mb-12">
        Register
      </div>
      
      {/* user name */}
      <label htmlFor='name' className="text-gray-300 text-xl mt-4 block">
      What should we call you?
      </label>
      <input id='name' type="input" placeholder='User Name' value={User.username} onChange={(e) => {setUser({...User, "username": e.target.value})}} className='bg-gray-300 rounded-md p-2 mt-2 w-72'/>
      
      {/* e-mail */}
      <label htmlFor='mail' className="text-gray-300 text-xl mt-4 block">
        Your E-mail
      </label>
      <input id='mail' type="email" placeholder='E-mail' value={User.email} onChange={(e) => {setUser({...User, "email": e.target.value})}} className='bg-gray-300 rounded-md p-2 mt-2 w-72'/>

      {/* password */}
      <label htmlFor="pass" className='text-gray-300 text-xl mt-8 block'>
        Your password
      </label>
      <input id='pass' type='password' placeholder="password" value={User.password} onChange={(e) => {setUser({...User, "password": e.target.value})}} className='bg-gray-300 rounded-md p-2 mt-2 w-72' />

      {/*  button  */}
      <button type='submit' onClick={RegiserRequest} className=' text-gray-200 bg-cyan-700 hover:bg-cyan-900 rounded-md px-4 py-2 my-8 w-72 block' >
        Create an account
      </button>
      <div className="text-gray-200">
        Already have an account?&nbsp;
          <Link to="/login">
            <span className="text-blue-500">
              Login here
            </span>
          </Link>
          
      </div>
    </div>
  </div>
</>
  )
}

export default Register