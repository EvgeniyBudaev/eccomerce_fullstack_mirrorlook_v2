import { combineReducers } from 'redux'
import {catalogReducer} from "./catalogReducer"
import {productListReducer} from "./productListReducer"

const rootReducer = combineReducers({
    catalog: catalogReducer,
    productList: productListReducer,
})

type RootReducerType = typeof rootReducer
export type RootStateType = ReturnType<RootReducerType>

export { rootReducer }