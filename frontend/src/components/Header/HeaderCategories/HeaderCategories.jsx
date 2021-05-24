import React, {useEffect} from 'react'
import {NavLink} from 'react-router-dom'
import {useDispatch, useSelector} from "react-redux"
import {ROUTES} from '../../../routes'
import {fetchCatalog} from "../../../redux/actions/catalogAction"
import Loader from "../../Loader"
import styles from './HeaderCategories.module.scss'

const HeaderCategories = () => {
    const dispatch = useDispatch()
    const catalogList = useSelector(state => state.catalog)
    const {loading, loaded, error, catalog} = catalogList

    useEffect(() => {
        if (!loading && !loaded) {
            dispatch(fetchCatalog())
        }
    }, [loading, loaded, dispatch])

    return (
        <>
            {
                loading || !loaded ? <Loader/>
                    : error ? <p>{error}</p>
                    :
                    <ul className={styles.headerCategories}>
                        {catalog.map(({id, name, catalogSlug}) => (
                            <NavLink
                                to={ROUTES.CATALOG + catalogSlug + '/'}
                                key={id} activeClassName={styles.active}>
                                <li
                                    className={styles.item}
                                >
                                    {name}
                                </li>
                            </NavLink>
                        ))}
                    </ul>
            }

        </>
    )
}

export default HeaderCategories