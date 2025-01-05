import SHSDASHBOARD from './pages/shsdashboard/dashboard';

function App() {
  return (
    <div className='w-full h-full  flex flex-wrap'>
      <div className='w-full p-5 flex flex-wrap gap-y-3'>
      <h1 className='text-5xl font-bold w-full text-center '>SENIOR HIGH SCHOOL ENROLLMENT DATA IN ALL REGIONS AND SECTORS</h1>
      <h1 className='w-full text-xl text-center font-thin'>YEAR 2016 - 2021</h1>
      <h1 className='w-full text-l text-center'>Charles Denver Ean Torres</h1>
      </div>
      <SHSDASHBOARD />
    </div>
  );
}

export default App;
