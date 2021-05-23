import { combineReducers } from 'redux'
import {catalogReducer} from "./catalogReducer"

const rootReducer = combineReducers({
    catalog: catalogReducer,
})


type RootReducerType = typeof rootReducer
export type RootStateType = ReturnType<RootReducerType>


export { rootReducer }