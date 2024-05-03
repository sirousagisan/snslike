import { useContext } from 'react'
import { Navigate, Outlet } from 'react-router-dom'

import { IsLoginContext } from '../contexts/UserContext'

const PrivateLayout = () => {
  const { isLogin}= useContext(IsLoginContext)
  console.log(isLogin);
  if (!isLogin) {
    return <Navigate to="/login"/>
  }
  return (
    <Outlet />
  )
}

export default PrivateLayout