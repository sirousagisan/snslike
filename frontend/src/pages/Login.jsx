import React, { useState, useEffect } from 'react'
import axios from "axios"

import { Link, useNavigate } from 'react-router-dom'

const Login = () => {
  const [ User, setUser ] = useState({"username": "", "password": ""})
  const navigate = useNavigate()
  useEffect(() => {
    const getCsrf = async () => {
      // const { data } = await axios.get(
      //   "http://127.0.0.1:8080/getcsrftoken",
      //   {withCredentials: true}
      // )
      axios.defaults.headers.common['x-csrftoken'] = "tl7vthygIGGH7e63GOeUeEVNFGmhgTW1"
    }
    getCsrf()
  }, [])
  const Login = async () => {
    await axios.post("http://127.0.0.1:8080/auth/login", User,
  {withCredentials: true}).then((res) => {
    setUser({"username": "", "password": ""})
    navigate("/")
  }).catch((res) => {
    console.log(User)
  })
  }
  return (
<>
<div className="flex justify-center items-center h-screen">
    <div className="border-2 rounded-xl py-8 px-12">
      <div className="text-gray-300 text-3xl mb-12">
        Login
      </div>
      
      {/* e-mail */}
      <label htmlFor='name' className="text-gray-300 text-xl mt-4 block">
        Your User Name
      </label>
      <input id='name' type="input" placeholder='User name' value={User.username} onChange={(e) => {setUser({...User, username: e.target.value})}} className='bg-gray-300 rounded-md p-2 mt-2 w-72'/>

      {/* password */}
      <label htmlFor="pass" className='text-gray-300 text-xl mt-8 block'>
        password
      </label>
      <input id='pass' type='password' placeholder='password' value={User.password} onChange={(e) => {setUser({...User, password: e.target.value})}} className='bg-gray-300 rounded-md p-2 mt-2 w-72' />

      {/*  button  */}
      <button onClick={Login} type='submit' className=' text-gray-200 bg-cyan-700 hover:bg-cyan-900 rounded-md px-4 py-2 my-8 w-72 block' >
        Submit
      </button>
      <Link to="/register">
        <span className="text-gray-200">
          Don’t have an account yet?&nbsp;
        </span>
        <span className='text-blue-500'>
          Register
        </span>
      </Link>
    </div>
  </div>
</>
  )
}

export default Login