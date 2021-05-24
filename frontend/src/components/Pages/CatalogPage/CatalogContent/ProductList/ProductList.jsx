import React, {useEffect} from 'react'
import {useDispatch, useSelector} from "react-redux"
import styles from './ProductList.module.scss'
import {fetchProductsByCatalog} from "../../../../../redux/actions/productListAction"


const ProductList = ({catalogSlug}) => {
    const dispatch = useDispatch()
    const products = useSelector(state => state.productList)
    console.log("products", products)

    useEffect(() => {
        dispatch(fetchProductsByCatalog(catalogSlug))
    }, [dispatch, catalogSlug])

    return (
      <ul className={styles.productList}>
        {/*{products && products.map(product => <Card key={product.id} product={product} />)}*/}
      </ul>
    )
}

export default ProductList