import React from 'react'

import { Link } from 'react-router-dom'

const Login = () => {
  return (
<>
<div className="flex justify-center items-center h-screen">
    <div className="border-2 rounded-xl py-8 px-12">
      <div className="text-gray-300 text-3xl mb-12">
        Login
      </div>
      
      {/* e-mail */}
      <label htmlFor='mail' className="text-gray-300 text-xl mt-4 block">
        Your E-mail
      </label>
      <input id='mail' type="email"  className='bg-gray-300 rounded-md p-2 mt-2 w-72'/>

      {/* password */}
      <label htmlFor="pass" className='text-gray-300 text-xl mt-8 block'>
        password
      </label>
      <input id='pass' type='password' className='bg-gray-300 rounded-md p-2 mt-2 w-72' />

      {/*  button  */}
      <button type='submit' className=' text-gray-200 bg-cyan-700 hover:bg-cyan-900 rounded-md px-4 py-2 my-8 w-72 block' >
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