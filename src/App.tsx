import Sidebar from './components/sidebar/sidebar';
import SHS from './pages/shsgraphs/shs';

function App() {
    return (
        <div className='w-full bg-green-200 flex'>
          <div className='w-1/5 bg-orange-300'>
            <Sidebar/>
          </div>
          <div className='w-4/5 bg-blue-100'>
            <SHS/>
          </div>
        </div>
    );
}

export default App;