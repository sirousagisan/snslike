import { Routes, Route } from "react-router-dom"

import Main from "./pages/Main"
import Login from "./pages/Login"
import Register from "./pages/Register"

import PrivateLayout from "./components/PrivateLayout"
function App() {

  return (
  <>
  <Routes>
    <Route element={<PrivateLayout />}>
      <Route path="/" element={<Main />}/>
    </Route>
    <Route path="/login" element={<Login />} />
    <Route path="/register" element={<Register />} />
  </Routes>
    {/* <Main /> */}
  </>
  )
}

export default App
