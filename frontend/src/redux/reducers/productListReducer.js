import {
    PRODUCT_LIST_FAILURE,
    PRODUCT_LIST_REQUEST,
    PRODUCT_LIST_SUCCESS
} from "../../constants/productListConstants"

const initialState = {
  loading: false,
  loaded: false,
  error: null,
  products: [],
}

export const productListReducer = (state = initialState, action) => {
    switch (action.type) {
        case PRODUCT_LIST_REQUEST:
            return {
                ...state,
                loading: true,
                loaded: false,
                error: null
            }

        case PRODUCT_LIST_SUCCESS:
            return {
                ...state,
                loading: false,
                loaded: true,
                products: action.payload
            }

        case PRODUCT_LIST_FAILURE:
            return {
                ...state,
                loading: false,
                loaded: false,
                error: action.payload
            }


        default:
            return state
    }
}