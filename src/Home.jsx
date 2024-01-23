import React from 'react';
import { Canvas } from '@react-three/fiber';

import Sky from './Models/Sky.jsx';
import Game from './Game.jsx';


const Home = () => {
    return (
        <div className='w-full h-screen relative'>
            <div className='flex justify-center absolute top-16 z-10 left-0 right-0'>
                <Game/>
            </div>
            <Canvas className='w-full h-screen'>
                <Sky/>
            </Canvas>      
        </div>
    )
}

export default Home