import { React, useState, useRef, useEffect } from 'react';

import img1 from './Assets/Photos/1 Steps.png';
import img2 from './Assets/Photos/2 Steps.png';
import img3 from './Assets/Photos/3 Steps.png';
import img4 from './Assets/Photos/4 Steps.png';
import img5 from './Assets/Photos/5 Steps.png';
import img6 from './Assets/Photos/Game Over.png';
import content from './Assets/Data/Data.json';

const Image = (steps) => {
    if (steps === 5 ){
        return img5;
    } else if (steps === 4 ){
        return img4;
    } else if (steps === 3 ){
        return img3;
    } else if (steps === 2 ){
        return img2;
    } else if (steps === 1 ){
        return img1;
    } else {
        return img6;
    }
}

const GetWordAndHint = () => {
    let randomNumber = Math.floor(Math.random() * Object.keys(content.answer).length)
    let word = content.answer[randomNumber]
    let hint = content.hint[randomNumber]
    return{
        word: word,
        hint: hint
    }
}

const Game = () => {
    const [steps, setSteps] = useState(5);
    const [letter, setLetter] = useState('')
    const [word, setWord] = useState('')
    const [letterArray, setLetterArray] = useState([])
    const [gameMessage, setGameMessage] = useState('Welcome')
    const [answer, setAnswer] = useState(GetWordAndHint)
    const [gameFinish, setGameFinish] = useState(false)

    const letterRef = useRef(null)
    const wordRef = useRef(null)

    const GetProgress = (word, guessed) => {

        let correct = ""
        let correctCount = 0
    
        for (let letter of word){
            if (guessed.includes(letter.toUpperCase())){
                correct = correct + letter
                correctCount++
            } else {
                correct = correct + '_ '
            }
        }

        useEffect(() => {
            if(correctCount === word.length){
                setGameFinish(true)
            }
        }, [correctCount,setGameFinish])

        return correct
    }

    const handleLetterSubmit = (e) => {
        e.preventDefault(); 


        const upperCaseLetter = letter.toUpperCase();

        if(/^[A-Za-z]$/.test(letter)){
                if (letterArray.includes(upperCaseLetter)){
                    setGameMessage('You Have Already Selected '+ upperCaseLetter + ' Try Again')
                } else {
                    if (answer.word.includes(upperCaseLetter)){
                        setLetterArray([...letterArray, upperCaseLetter]);
                        setGameMessage('You inputted: '+ upperCaseLetter + ', Correct')
                    } else {
                        setLetterArray([...letterArray, upperCaseLetter]);
                        setGameMessage('You inputted: '+ upperCaseLetter + ', Wrong')
                        setSteps(steps-1)
                    }
                }
        } else {
            setGameMessage('Invalid Input')
        }

        
        
        letterRef.current.value = ''
        setLetter('')
        
    };

    const handleWordSubmit = (e) => {
        e.preventDefault();

        if (word.toUpperCase() === answer.word){
            setGameMessage('You inputted: '+ word + ', Correct')
            setLetterArray(word.toUpperCase())
            setGameFinish(true)
        } else {
            setGameMessage('You inputted: '+ word + ', Wrong')
            setSteps(steps-1)
        }
        wordRef.current.value = ''
        setWord('')
    }

    const RestartButton = () => {
        setAnswer(GetWordAndHint)
        setLetterArray([])
        setSteps(5)
        setGameMessage('Welcome Back')
        letterRef.current.value = ''
        setLetter('')
        wordRef.current.value = ''
        setWord('')
        setGameFinish(false)
    }

    const GameOver = (steps) => {
        if (steps === 0){
            return (true)
        } else {
            return (false)
        }
    }

    return (
        <div className='Container min-w-80 max-w-96 bg-transparent flex flex-col'>
            <div className='GameTab p-1 rounded-t-md bg-slate-300'>        
                <h1 className='GameTabMessage flex item-center justify-center'>PROTECT THE CHEESE</h1>
            </div>
            <div className='GameMain flex flex-col justify-center items-center w-full max-w-96 rounded-b-md bg-slate-200 bg-opacity-80 p-2'>
                <h1 className='GameTitle font-bold'>PROTECT THE CHEESE</h1>
                <p className='GameHint rounded-md bg-white w-48 h-12 p-1 mt-3 text-sm'>Hint: {answer.hint}</p>
                <p className='GameMessage rounded-md bg-white w-48 h-12 p-1 mt-3 text-sm text-slate-500'>{gameMessage}</p>
                    <div className='GameImage mt-3'>
                        <img src={Image(steps)} className='w-48 h-48'></img>
                    </div>
                <p className='GameProgress rounded-md bg-white w-48 h-6 px-2 mt-3 text-md font-bold'>{GetProgress(answer.word, letterArray, setGameFinish)}</p>

                <div className='GameInput w-48 mt-3'>
                    
                    <form className='flex flex-col justify-center items-center'>
                        <input 
                            className='mt-3 px-2 w-48 rounded-md text-slate-600' 
                            type="text" 
                            placeholder={GameOver(steps) ? 'GAME OVER' : (gameFinish ? 'Well Done' : 'Letter Input')}
                            onChange={(e) => setLetter(e.target.value)}
                            ref={letterRef} 
                            disabled={GameOver(steps)||gameFinish}
                            />

                        <button 
                            className='w-24 mt-2 bg-slate-300'
                            onClick={handleLetterSubmit}
                            disabled={GameOver(steps)||gameFinish}
                            >Submit</button>
                    </form>

                    <form className='flex flex-col justify-center items-center'>
                        <input 
                            className='mt-3 px-2 w-48 rounded-md text-slate-600' 
                            type="text" 
                            placeholder={GameOver(steps) ? 'GAME OVER' : (gameFinish ? 'Well Done' : 'Word Input')}
                            onChange={(e) => setWord(e.target.value)}
                            ref={wordRef}
                            disabled={GameOver(steps)|| gameFinish}
                            />

                        <button 
                            className='w-24 mt-2 bg-slate-300'
                            onClick={handleWordSubmit}
                            disabled={GameOver(steps)||gameFinish}
                            >Submit</button>
                    </form>

                </div>
                    <button 
                        className='w-24 mt-5 bg-slate-300'
                        onClick={RestartButton}
                        style={GameOver(steps) || gameFinish ? { backgroundColor: '#e6f4d7' } : {}}
                        >RESTART</button>
            </div>
        </div>
    ) 
}

export default Game