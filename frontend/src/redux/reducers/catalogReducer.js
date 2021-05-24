import {
    CATALOG_FAILURE,
    CATALOG_REQUEST,
    CATALOG_SUCCESS
} from "../../constants/catalogConstants"

const initialState = {
  catalog: [],
  loading: false,
  loaded: false,
  error: null,
}

export const catalogReducer = (state = initialState, action) => {
    switch (action.type) {
        case CATALOG_REQUEST:
            return {
                ...state,
                loading: true,
                loaded: false,
                error: null
            }

        case CATALOG_SUCCESS:
            return {
                ...state,
                loading: false,
                loaded: true,
                catalog: action.payload
            }

        case CATALOG_FAILURE:
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