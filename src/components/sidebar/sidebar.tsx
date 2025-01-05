import React from 'react';

const Sidebar: React.FC = () => {
  return (
    <div className='fixed h-full bg-transparent w-2/12'>
      <div className='text-5xl p-4'>
        Dashboard
      </div>
      <div className='flex flex-col w-full bg-green-500'>
        <a className='w-full p-4' href=''>Home</a>
        <a className='w-full p-4' href=''>Home</a>
        <a className='w-full p-4' href=''>Home</a>
        <a className='w-full p-4' href=''>Home</a>
      </div>
    </div>
  );
};

export default Sidebar;
